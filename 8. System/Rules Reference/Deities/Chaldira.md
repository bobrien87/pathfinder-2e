---
type: deity
source-type: "Remaster"
domains: "Confidence, Luck, Trickery, Zeal"
favored-weapon: "Shortsword"
divine-font: "Heal"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Fleet Step]], Rank 2: [[Laughing Fit]], Rank 5: [[Cloak Of Colors]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Chaldira Zuzaristan, the Calamitous Turn, is a plucky, impulsive goddess venerated primarily by halflings. She embodies two aspects halflings see in themselves: a strong affinity for luck and a bold determination to protect friends. Chaldira is hotheaded and cannot abide bullies in any form, and many of her worshippers are similarly impetuous, spoiling for any opportunity to leap fist-first at oppressors and tyrants. While many people consider this to be more of a vice than a virtue, Chaldira and her followers feel it is far better to run headlong into trouble than it is to meekly concede to evil out of fear or convenience. Chaldira is also the goddess of light-hearted mischief, insisting that harmless fun, even at others' expense, brings joy and strengthens ties within a community. While not all of Chaldira's followers are inveterate pranksters, most at least know some sleight-of-hand tricks.

**Title** The Calamitous Turn

**Areas of Concern** battle, fortune, mischief

**Edicts** seek out and challenge oppressors and tyrants, defend friends and the innocent, engage in mischief that doesn't harm others

**Anathema** suffer a bully's insult to you or another without retort, abandon a friend in need, attribute a lucky turn of events to your own skill

**Religious Symbol** shortsword with three notches

**Sacred Animal** lizard

**Sacred Color** green, red

**Source:** `= this.source` (`= this.source-type`)
