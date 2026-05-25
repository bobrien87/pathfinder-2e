---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Emotion]]", "[[Fear]]", "[[Incapacitation]]", "[[Magical]]", "[[Mental]]", "[[Prediction]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 500, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Carvings of skulls, monsters, and all manner of violence decorate this wand of blackened bone, but it makes absurd sounds when Activated, such as a honking horn, a manic giggle, or a daydreamy sigh.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast 3rd-rank [[Impending Doom]], showing the target a potential death that's gruesome and absurd. If the target becomes [[Frightened]] by the spell, it also becomes [[Stupefied]] with a value 1 higher than the frightened value. This lasts for the duration of the spell.

**Craft Requirements** Supply a casting of *impending doom* of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
