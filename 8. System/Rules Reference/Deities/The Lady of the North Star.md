---
type: deity
source-type: "Remaster"
domains: "Cold, Darkness, Secrecy, Vigil"
favored-weapon: "Glaive"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 2: [[Stupefy]], Rank 6: [[Blanket Of Stars]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

A goddess whose name has been lost to time (or purposefully obscured), the secretive Lady of the North Star is referred to only by her countless epithets. Despite the efforts of Pharasma's faithful to scrub the Lady's name from the annals of history, a few scattered sects still worship her and transmit her teachings. Their ranks are often closed to outsiders, and their initiation rituals are arduous and famously cryptic. In spite of the Lady of the North Star's love for secrecy, she has one famous weakness: her empathy for those nearing death. She has been known to take pity on those afflicted with incurable curses and ailments of all kinds, appearing to prospective followers through dreams and visions. There, she presents them with a final challenge: to uncover her lost path to immortality before their time runs out.

**Title** Mother of Secrets

**Areas of Concern** Secrets, remembrance, winter, immortality

**Edicts** Seek lost knowledge, uncover hidden mysteries, honor that which is forgotten, pursue immortality

**Anathema** Destroy sources of knowledge, make public that which should remain secret, desecrate a memorial, grow complacent about one's ignorance and mortality, commit torture or murder, knowingly harm an innocent

**Religious Symbol** jade cicada floating over mercury

**Sacred Animal** peafowl

**Sacred Colors** silver, violet

**Source:** `= this.source` (`= this.source-type`)
