---
type: deity
source-type: "Remaster"
domains: "Family, Freedom, Might, Protection"
favored-weapon: "Machete"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Animal Form]], Rank 4: [[Mountain Resilience]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Kazutal, also known as Mother Jaguar or Lady Jaguar, is an old deity, revered for thousands of years on the continent of Arcadia. Ages ago, she was worshipped in the Razatlani Empire as a goddess of might and protection in war. After the catastrophe of Earthfall, however, her edge softened; those who struggled to put the world back together called upon her to protect their neighbors and came together under her guidance to build strong bonds of community and support.

Today, Kazutal is worshipped throughout Arcadia as a deity of community, liberty, and safety. Her churches support the downtrodden and reinforce better ways to work alongside one another for compassionate goals. Clerics of Kazutal ask her for strength so they can help those around them and protect them from danger, enriching their communities with civic pride and keeping a sharp eye out for internal dangers and bad actors among their flock. Warpriests of Kazutal rely on the deadly edge of their machetes to fight against corrupting and oppressive forces in the world. Above all, Kazutal's clergy preaches the strength of love, both for other people and the cultures they form, which gives followers the strength to fight without compromise or weakness to protect those they hold dear.

**Title** Mother Jaguar

**Areas of Concern** safety, liberty, community

**Edicts** defend your people, provide for those who need you, oppose those who unjustly lord power over others, demonstrate devotion to things you love

**Anathema** own a slave, force a creature to act against its will, refuse to give aid to an ally, enforce an unjust law

**Religious Symbol** jaguar's head on a green circle

**Sacred Animal** jaguar

**Sacred Color** black, gold, green

**Source:** `= this.source` (`= this.source-type`)
