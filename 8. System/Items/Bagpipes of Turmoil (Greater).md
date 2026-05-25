---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 460}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

While those who appreciate bagpipes may like the sound of this gray reed and black leather instrument, its real purpose is to sow turmoil against a performer's enemies, spreading discord with each note. While playing the bagpipes, you gain a +1 item bonus to Performance checks and to Intimidation checks made to [[Demoralize]].

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrip** [[Daze]]
- **1st** [[Bane]]
- **2nd** [[Deafness]], [[Knock]], [[Shatter]]
- **3rd** [[Paralyze]], [[Shift Blame]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
