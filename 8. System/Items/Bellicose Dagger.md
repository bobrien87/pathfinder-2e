---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Agile]]", "[[Cursed]]", "[[Finesse]]", "[[Magical]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The hilt of a bellicose dagger is etched with the word for "war" in various languages. Having absorbed the spirit of violence over the course of its existence, the weapon now craves bloodshed. A bellicose dagger is a *+1 striking wounding dagger*. However, anytime you interact with creatures, no matter the context, you must succeed at a DC 25 [[Will]] save or else find you have, as a reaction, drawn the dagger.

When you use the bellicose dagger as a weapon for the first time, it fuses to you. While it's in your possession, you take a –2 circumstance penalty to Diplomacy checks and skill checks to avoid fighting, such as Deception checks to trick your way out of a scuffle or Stealth checks to sneak past enemies.

**Source:** `= this.source` (`= this.source-type`)
