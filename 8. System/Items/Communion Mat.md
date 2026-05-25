---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 3750}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This pageless grimoire is made up of two durable covers that open to display a small ritual circle. When you first invest the grimoire, you and your familiar each press a limb to a corner of the mat. The ritual circle then morphs to one matching the tradition of your patron, the spells contained in your familiar appearing in the margins. During your daily preparations, your familiar performs a small jaunt around the open ritual circle to strengthen its connection to your patron.

**Activate** `pf2:f` (concentrate, spellshape)

**Frequency** once per 10 minutes

**Effect** If your next action is to cast a spell your familiar learned from a lesson (whether a cantrip or from a spell slot), your patron notices that you're putting their power to good use and strengthens your familiar with a surge of magic. Your familiar Sustains one of your spells.

**Source:** `= this.source` (`= this.source-type`)
