---
type: deity
source-type: "Remaster"
domains: "Death, Knowledge, Travel, Vigil"
favored-weapon: "Club"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Tailwind]], Rank 2: [[Knock]], Rank 6: [[Teleport]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Appearing as an enormous migratory bird—usually a corvid, but sometimes a songbird—draped in robes and carrying a tombstone lock and a giant bone key, Barzahk the Passage is the psychopomp usher who maintains the Dead Roads, the secret back routes between the planes and the mortal world. Among mortals, they are worshipped as a patron of compasses, travelers, and vigils. Barzahk is tasked with transporting the souls of those who die far from home to ensure that they reach their proper destination. Unfortunately, Barzahk wanders far and wide, and so they rarely attend to this duty. Thus Barzahk's followers, both psychopomps and mortals, take it upon themselves to care for lost souls, both literal and figurative. Like their patron, followers of Barzahk are often migratory, helping those they find along the way.

**Title** The Passage

**Areas of Concern** Compasses, travelers, vigils

**Edicts** Aid travelers and those who return from the dead, tend to roadside graves, find missing objects or people

**Anathema** Celebrate specific calendar dates over others, avoid travel or change, freeze time for an object or creature

**Religious Symbol** two straight lines that converge vertically through a circle

**Sacred Animal** migratory birds

**Sacred Colors** black, gray

**Source:** `= this.source` (`= this.source-type`)
