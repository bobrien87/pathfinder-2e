---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Monk]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1820}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This ash wood staff is topped by a long tassel of bleachedwhite horsehair. Historically carried by the most important of court officials throughout various regions and periods of Tian Xia's history, purgatory emissary's staves are also strongly associated with psychopomps serving punitive sentences. It's thought this connection is a comical nod to the bureaucratic nature of the afterlife.

Psychopomps and spirits tend to regard you with a level of respect while you carry a purgatory emissary's staff. While you wield this staff, you receive a +2 item bonus to all skill checks to adjust a psychopomp's or spirit's attitude.

When used as a weapon, a purgatory emissary's staff is a *+2 striking ghost touch staff*.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Vitality Lash]]
- **1st** [[Command]], [[Sanctuary]]
- **2nd** [[Clear Mind]], [[See the Unseen]]
- **3rd** [[Holy Light]], [[Ring of Truth]]
- **4th** [[Dispel Magic]], [[Talking Corpse]]
- **5th** [[Banishment]], [[Truespeech]]

**Source:** `= this.source` (`= this.source-type`)
