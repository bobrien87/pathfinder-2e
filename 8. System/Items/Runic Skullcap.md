---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Divine]]", "[[Focused]]", "[[Invested]]", "[[Mythic]]"]
price: "{'gp': 6000}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This silver skullcap is etched with snake patterns and a single Sihedron rune. The skullcap grants a +2 item bonus to Arcana and Religion checks. If a check is attempted to [[Recall Knowledge]] about rune magic or Lissala, the wearer treats the results of a failure or critical failure as one degree of success better.

**Activate—Rewards of Service** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** Gain 1 Focus Point, which you can spend only to cast a cleric domain spell for a domain belonging to Lissala. Lissala's domains are ambition, duty, fate, and knowledge. If you don't spend this point by the end of this turn, it is lost.

**Activate—Rewards of Rule** 1 minute (concentrate)

**Requirements** You have master or legendary proficiency in Arcana

**Effect** Spend 1 Mythic Point when you invest the runic skullcap. Until the next time you invest the skullcap, you can also use the Focus Point granted by Rewards of Service to cast a focus spell from the runelord wizard school.

- **Envy:** [[Cutting Eye]]
- **Greed:** [[Precious Gleam]]
- **Sloth:** [[Reclined Apport]]
- **Gluttony:** [[All Encompassing Hunger]]
- **Lust:** [[Heart's Hook]]
- **Pride:** [[Crescent Scepter]]
- **Wrath:** [[Vengeful Glare]]

**Source:** `= this.source` (`= this.source-type`)
