---
type: deity
source-type: "Remaster"
domains: "Duty, Family, Freedom, Protection"
favored-weapon: "Spear"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Endure]], Rank 4: [[Soft Landing]], Rank 6: [[Collective Transposition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

For those who have lost everything, or who have never had it to lose, even the smallest kindness can mean the world. Lorris and his followers work to create these kindnesses, knowing that they can elevate the attitude of the most downtrodden. This can be as little as carrying candies in their pockets to share with those they meet, or larger gestures such as opening their homes to those who would not have a place of their own to safely lay their heads. Some even choose to go through the process of adopting orphans, welcoming them into their family as their own. Lorris has the appearance of a man with dark skin with a white hound's head and clad in a simple beggar's robe that never seems to dirty. He's also known to take on the form of a droopy-eyed hound dog who drops off small meals to starving street children, rather than allowing them to continue begging for scraps.

**Title** The Savior Hound

**Areas of Concern** Charity, the disadvantaged, orphans, volunteering

**Edicts** Give to those less fortunate than you, help orphans find safe housing, assist those in need

**Anathema** Ignore the needs of others when they ask for your help, take from widows or orphans, contribute to the destruction of housing for the unfortunate

**Religious Symbol** howling dog on coin

**Sacred Animal** hound

**Sacred Colors** brown, gold

**Source:** `= this.source` (`= this.source-type`)
