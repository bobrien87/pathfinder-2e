---
type: deity
source-type: "Remaster"
domains: "Destruction, Knowledge, Magic, Protection"
favored-weapon: "Staff"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Force Barrage]], Rank 2: [[Embed Message]], Rank 3: [[Levitate]], Rank 4: [[Flicker]], Rank 5: [[Telekinetic Haul]], Rank 6: [[Wall Of Force]], Rank 7: [[Warp Mind]], Rank 8: [[Quandary]], Rank 9: [[Detonate Magic]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ancient Osirion legends speak of the god-king Nethys, an ancient mortal who studied under the greatest Osirian priest scribes, who in turn were eager to nurse his love of knowledge and magic. He was a mortal man who later mastered the divine, then the occult, then searched all planes of existence to one day learn all knowledge of magic that there could ever be. No one knows how long this journey took, only that he succeeded, and at once realized that his mortal body could not possibly contain all the knowledge and power at his disposal. He ascended to godhood immediately upon this realization, since he had the knowledge of how to do so already. This allowed him to retain his magic and perfect knowledge without having to lose any of it to mental degradation. For Nethys, godhood was a necessity, a way to maintain what he had learned, never to lose a memory ever again.

**Title** The All-Seeing Eye

**Areas of Concern** magic

**Edicts** seek out magical power and use it

**Anathema** continually pursue mundane paths over magical ones

**Religious Symbol** two-toned mask

**Sacred Animal** zebra

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
