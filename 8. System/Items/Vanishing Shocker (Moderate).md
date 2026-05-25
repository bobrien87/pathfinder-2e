---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Electricity]]", "[[Gadget]]", "[[Illusion]]", "[[Magical]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

The vanishing shocker is a cube with extruding spikes at each corner. This inscrutable device channels occult energy through the electricity it produces, creating the result of invisible lighting. When activated, the cube floats above your head, creating a field of invisible electricity in a @Template[type:emanation|distance:10] that lasts for 1 round. You and creatures within the emanation are [[Concealed]]. Creatures that enter or start their turn within the area must attempt a DC 27 [[Reflex]] save.
- **Success** The target is unaffected.
- **Failure** The target is [[Off Guard]] for 1 round.
- **Critical Failure** The target is [[Clumsy]] 1 and off-guard for 1 round.

**Source:** `= this.source` (`= this.source-type`)
