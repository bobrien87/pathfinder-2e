---
type: deity
source-type: "Remaster"
domains: "Death, Magic, Nightmares, Repose"
favored-weapon: "Staff"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Ill Omen]], Rank 3: [[Paralyze]], Rank 5: [[Wave Of Despair]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

All mortals must die. This is the empirical truth championed by Chamiaholom, whose mission is to remind mortals that they will one day meet their end. Chamiaholom's form is a towering skeleton over 14 feet tall, wielding a staff made from the skulls of his victims. He is sometimes glimpsed around sites of tragedy and destruction and stalks those who've survived near-death experiences, terrifying witnesses who mistake him for death incarnate. Chamiaholom's followers wear dark paint on their faces to imitate the tormentor's skeletal visage as they travel around Golarion preaching their message of despair.

**Title** Skull Staff

**Areas of Concern** Domination, hopelessness, mortality

**Edicts** Accept the futility of life, destroy sentient undead, punish those who somehow avoid death

**Anathema** Comfort the dying, seek immortality or unnatural longevity

**Religious Symbol** staff made of skulls

**Sacred Animal** maggot

**Sacred Colors** gray, black, white

**Source:** `= this.source` (`= this.source-type`)
