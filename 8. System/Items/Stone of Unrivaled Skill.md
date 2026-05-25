---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Contract]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "other"
bulk: "—"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You traded your senses to a hag for unrivaled expertise stolen from various souls who were once the greatest in their field. Your *bargained contract* is sealed by sleeping with a pitch-black stone under your pillow every night. Choose one skill when you seal this *bargained contract*. You become an expert in that skill; if you were already an expert, you become a master, and if you were already a master, you become legendary. Once per day, from any distance, the hag that holds your contract can take over your senses for 10 minutes, during which time the hag hears, sees, smells, tastes, and feels everything you would typically experience. During this time, you're [[Dazzled]] by your own disjointed senses.

**Activate—Taste Fluency** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You place the stone sealing your *bargained contract* in your mouth. For the next 10 minutes, you gain a +3 status bonus to skill checks using the skill you chose for your contract.

**Source:** `= this.source` (`= this.source-type`)
