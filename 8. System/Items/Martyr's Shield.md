---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Divine]]", "[[Intelligent]]"]
price: "{'value': {}}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +12; precise vision 30 feet, imprecise hearing 30 feet

**Communication** speech (Common and Empyrean)

**Skills** Diplomacy +15, Religion +13

**Int** +0, **Wis** +2, **Cha** +4

**Will** +15

A *martyr's shield* is a *lesser sturdy shield* imbued with the compassion of a devout champion of a righteous deity, like Iomedae or Vildeis, who sacrificed themself to save an ally. In addition to good-naturedly attempting to convert you to its religion, the *martyr's shield* can use 1 reaction each round that, when raised, it uses to Shield Block to protect an ally adjacent to you. This follows the rules for Shield Block, but protects your ally instead. The *martyr's shield* uses this reaction whether you would prefer it did so or not. The *martyr's shield* can be upgraded to a stronger form of *sturdy shield* by paying the difference in cost between its current type of *sturdy shield* and the new type.

**Source:** `= this.source` (`= this.source-type`)
