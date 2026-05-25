---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Coda]]", "[[Occult]]", "[[Staff]]"]
price: "{'gp': 1900}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These panpipes are made of what seems to be beat-up tin bound by frayed leather and look like they shouldn't function at all, but in skilled hands they emit a beautiful sound that beguiles the senses. While playing the pipes, you gain a +2 item bonus to Diplomacy and Performance checks.

**Activate** Cast a Spell

**Effect** You expend a number of charges from this instrument to cast a spell from its list.

- **Cantrip** [[Daze]]
- **1st** [[Charm]], [[Command]], [[Fear]]
- **2nd** [[Laughing Fit]], [[Stupefy]]
- **3rd** [[Charm]], [[Hypnotize]], [[Mind Reading]], [[Ring of Truth]]
- **4th** [[Confusion]], [[Suggestion]]
- **5th** [[Charm]], [[Glimmer of Charm]], [[Suggestion]], [[Telepathy]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
