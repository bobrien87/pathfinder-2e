---
type: deity
source-type: "Remaster"
domains: "Change, Fate, Magic, Moon"
favored-weapon: "Chakri"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Ill Omen]], Rank 2: [[Animal Messenger]], Rank 3: [[Feet To Fins]], Rank 4: [[Bestial Curse]], Rank 5: [[Moon Frenzy]], Rank 6: [[Cursed Metamorphosis]], Rank 7: [[Warp Mind]], Rank 8: [[Migration]], Rank 9: [[Metamorphosis]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The sea hags of Kardaji Bay's eastern coast are infamous for offering dangerous bargains. Whatever the sea hag Zeaki offered the cyclopes of Hoimpeia remains a mystery, yet apparently it was too good to refuse. In return, they enacted a myth-speaking on her behalf. The hero-god now haunts Itia, an island south of Dhuraxilis, where she listens to petitioners, hoards secrets, and offers extraordinary magic for a price. On occasion, she even joins and empowers other covens, though misfortune often befalls these partners before Zeaki returns home.

Like the ocean's tides, Zeaki's appearance varies from day to day and for each visitor, and she happily shares some of her shapeshifting magic with the dysmorphic. Despite her sinister reputation as a hag, Zeaki engages most visitors with an open mind. Those who reciprocate find she's a civil host and mostly fair bargainer. However, anyone who insults or attempts to cheat her earns a terrible enemy, with forgiveness rarely granted except by performing some great service for the hag. The unrepentant often find themselves transformed into witless beasts, cursed to roam Itia.

**Title** The Matron of Metamorphoses

**Areas of Concern** tides and transformation

**Edicts** inflict poetic justice upon those who wrong you, assist others' personal transformations, learn esoteric secrets that others might value

**Anathema** become complacent with your current self, offer aid to a stranger without exacting some price (even if the cost isn't obvious)

**Religious Symbol** open hand with each finger from a different creature

**Sacred Animal** hermit crab

**Sacred Colors** brown, orange

**Source:** `= this.source` (`= this.source-type`)
