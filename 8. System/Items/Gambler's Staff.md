---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 2000}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A small glass orb on the head of a *gambler's staff* holds a pair of six-sided dice that shift and roll within. Spellcasters who make their living via games of chance use *gamblers' staves* to encourage the odds in their favor. Most gambling dens ban players they discover using such magic items. A *gambler's staff* grants you a +2 circumstance bonus to checks to [[Earn Income]] from gambling (typically using Games Lore). To get this benefit, the staff must be on your person during all the downtime you spend gambling.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Wash Your Luck]]
- **1st** [[Nudge the Odds]]
- **2nd** [[Lucky Number]]
- **3rd** [[Shift Blame]]
- **4th** [[Read Omens]], [[Winning Streak]]
- **5th** [[Nudge the Odds]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
