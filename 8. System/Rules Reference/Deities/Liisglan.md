---
type: deity
source-type: "Remaster"
domains: "Creation, Perfection, Time, Toil"
favored-weapon: "Dancers-spear"
divine-font: "Harm, Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Gravitational Pull]], Rank 4: [[Creation]], Rank 9: [[Detonate Magic]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

All things, regardless of what they are, have inherent rules that govern their shape, structure, how they react to outside forces, and so on. Liisglan maintains these rules, keeping them contained within their allowed parameters so as to maintain the orderly structure of existence as a whole. If a creature were to suddenly break these rules to become unaffected by gravity or unable to interact with solid objects without some kind of outside influence, it could lead to ultimate disaster. The rules are in place for a reason, and the Forces Within does not suffer any who try to break these rules.

**Title** The Force Within

**Areas of Concern** Governing physics, harmony, sequences

**Edicts** Uphold the laws of the physical and magical world, arrange things with orderly patterns or logic, make use of music during your work

**Anathema** break a rule of physics or magic, create discordant music, intentionally disrupt a non-detrimental pattern

**Religious Symbol** musical staff with a rising and dropping line

**Sacred Animal** cicada

**Sacred Colors** black, gold

**Source:** `= this.source` (`= this.source-type`)
