---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Auditory]]", "[[Consumable]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

Not only are the eggs of giant owls delicious when boiled, but when infused with a mix of alchemical reagents, they also make you emit a long and terrifying screech. All creatures in a @Template[emanation|distance:30] must attempt a DC 23 [[Will]] save. Regardless of the result, creatures in the area are temporarily immune to this screech for 1 minute.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 3 and [[Fleeing]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
