---
type: deity
source-type: "Remaster"
domains: "Ambition, Destruction, Might, Zeal"
favored-weapon: "Longbow"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Fireball]], Rank 4: [[Translocate]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hell's Valkyrie rules a domain spanning part of Dispater's realm, commanding her legions of infernal soldiers as she sees fit. Eiseth operates outside Dispater's rule, and she has forged powerful alliances both in Hell and beyond, having long ago rejected limitations placed upon her by others. Foremost among the Queens of the Night, she embodies battle, revenge, and wrath, and her ambitions are as lofty as her aerie of Widow's Cry, where she forges souls of the damned into unequaled infernal legions answering to her alone.

**Title** Hell's Valkyrie

**Areas of Concern** Battle, revenge, wrath

**Edicts** Avenge all insults, claim what you desire and deserve, humiliate your foes in ironic fashion

**Anathema** Allow a slight to go unanswered, show humility or fear

**Religious Symbol** horned longbow

**Sacred Animal** raven

**Sacred Colors** black, orange

**Source:** `= this.source` (`= this.source-type`)
