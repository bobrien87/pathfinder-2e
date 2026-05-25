---
type: deity
source-type: "Remaster"
domains: "Change, Confidence, Fate, Luck"
favored-weapon: "War-flail"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Ill Omen]], Rank 5: [[False Vision]], Rank 7: [[True Target]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

A dogmatic obsession with fate, luck, and patterns paints Bifrons as a questionable partner. They experience the highest highs and the lowest lows, celebrating each equally. Distinguishing whether windfall and forfeiture are brought by chance or inevitability is pointless to their mind, for it is all within the parameters of the universe's game. Their base is built on the teasing of mortals against the odds; if they lose, such only proves the pattern, while if they win, fate smiled upon them and they should thank Bifrons for their encouragement. Patrons of the Second Fate consider misfortune as an investment in greater rewards to come, gambling they'll be free to collect the consequences. Many promise to contract with the devil only temporarily, just until they've had enough. Few are able to satisfy this conviction, but Bifrons loves an underdog. Bifrons appears as a gambling devil, a devil made entirely of gold, clad in royal regalia with a face that appears to be either shouting in glee or screaming in agony.

**Title** The Second Fate

**Areas of Concern** Fate, luck, patterns

**Edicts** Steal coins from wells, bet on red, collect obscure oracular knick knacks

**Anathema** Take the same path twice, calculate your chances, dismiss superstition

**Religious Symbol** two-faced devil head

**Sacred Animal** fox

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
