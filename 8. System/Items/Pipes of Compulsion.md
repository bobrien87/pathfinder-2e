---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 90}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These panpipes are made of what seems to be beat-up tin bound by frayed leather and look like they shouldn't function at all, but in skilled hands they emit a beautiful sound that beguiles the senses. While playing the pipes, you gain a +1 item bonus to Diplomacy and Performance checks.

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrip** [[Daze]]
- **1st** [[Charm]], [[Command]], [[Fear]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
