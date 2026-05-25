---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 52}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell

Swirling sand carries a faint trace of strange compulsions from the helical sand spire near Beachcomber. Adding this catalyst to a [[Suggestion]] spell implants a strange compulsion in one target of the spell. The target creature must spin counterclockwise at the end of its turn if it didn't take a move action that turn. This spin is a free action that has the move trait. This effect lasts for 3 rounds on a success, failure, or critical failure against *suggestion* (even if the target completes its *suggestion* in fewer rounds); a target that critically succeeds against *suggestion* is unaffected by the swirling sand.

**Source:** `= this.source` (`= this.source-type`)
