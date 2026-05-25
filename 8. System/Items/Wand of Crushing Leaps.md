---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'cp': 0, 'gp': 80, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This supple, light wooden wand drifts to the ground like a feather or leaf when dropped, landing unharmed. A thin coil of metal wraps around the wand's handle.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You cast [[Jump]], but can jump up to 60 feet. When you land you shatter the ground, making each creature in a @Template[emanation|distance:5] [[Off Guard]] until the start of its next turn. In addition, the space you land in and all squares in the emanation become difficult terrain for 1 minute.

**Craft Requirements** Supply a casting of 1st-rank *[[Jump]]*.

**Source:** `= this.source` (`= this.source-type`)
