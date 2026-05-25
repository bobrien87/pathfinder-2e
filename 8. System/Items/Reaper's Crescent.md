---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Agile]]", "[[Finesse]]", "[[Light]]", "[[Trip]]"]
price: "{'gp': 575}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The blade of this alabaster *+1 striking sickle* grows thick and pitted as the moon waxes, and it thins to a sharp sliver as the moon wanes. Moonlight also causes a second rune on the blade to change shape with the moon's phases: during the new and crescent moon, the weapon has the *[[Ghost Touch]]* rune; during the quarter moon, the *[[Fearsome]]* rune; and during the gibbous and full moon, the *[[Wounding]]* rune.

When wielded under moonlight of any strength, the *reaper's crescent* deals additional cold damage equal to the number of damage dice.

**Source:** `= this.source` (`= this.source-type`)
