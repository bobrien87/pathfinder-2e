---
type: deity
source-type: "Remaster"
domains: "Cities, Freedom, Luck, Trickery"
favored-weapon: "Frying-pan"
divine-font: "Harm, Heal"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Grease]], Rank 2: [[Laughing Fit]], Rank 3: [[Mad Monkeys]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

No place where Cong appears remains calm. One can notice them from ten miles away due to their cacophonous presence. Cong, the Smash-crash, is one of the few goblin hero-gods who often presents themself in avatar form, and then only to those who have a great prank in mind and need an extra hand to carry it out. Cong's appearance is that of a goblin with a multitude of trinkets attached to every available part of their body, each a different instrument for noise or pranking. They are mainly popular among children and the most chaotic of goblins. Followers of Cong are often frowned upon by other ancestries, but most goblin tribes endorse these unbridled acts and get a good chuckle out of it. Many more goblins are punished for reacting badly to one of Cong's followers (or Cong themself) than punishment toward those who carry out such pranks. This is mostly because Cong's pranks are never done with the intention of harming other individuals, but rather for everyone else to get a big laugh out of it (though being goblins, the harmless intentions do not always translate into harmless acts).

**Title** The Smash-crash

**Areas of Concern** Cacophonies, mischief, tricks

**Edicts** Make yourself known, make fun of the unsuspecting

**Anathema** React poorly or offensively to mischief, silence loud noises

**Religious Symbol** pair of cymbals

**Sacred Animal** mockingbird

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
