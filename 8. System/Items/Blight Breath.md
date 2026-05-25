---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Air]]", "[[Bottled breath]]", "[[Consumable]]", "[[Magical]]", "[[Poison]]"]
price: "{'gp': 350}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This foul-smelling bottle contains compressed, noxious fumes. After you inhale the odious gases of the *blight breath*, you gain resistance 10 to poison for as long as you hold your breath. You can exhale the *blight breath* as a single action. The resulting spray of noxious fumes deals @Damage[10d6[poison]|options:area-damage] damage to each creature in a @Template[cone|distance:15], with a DC 29 [[Reflex]] save

> [!danger] Effect: Blight Breath

**Source:** `= this.source` (`= this.source-type`)
