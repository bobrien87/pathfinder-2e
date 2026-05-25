---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Dragonroots are pale, golden-rooted plants that grow throughout Tian Xia. Just as mandrake roots or ginseng roots are sometimes regarded to have almost humanoid shapes, these roots appear as if they were dragons. They're commonly used in the formulation of healing potions, but the most sought-after have grown for centuries, for they're viable for enchantment into *thousand-year dragonroots*.

When you activate a *thousand-year dragonroot*, your body shimmers with golden light, providing illumination as a torch. You gain a fly Speed of 40 feet and fire resistance 5 for 1 minute.

> [!danger] Effect: Thousand Year Dragonroot

**Source:** `= this.source` (`= this.source-type`)
