---
type: deity
source-type: "Remaster"
domains: "Cities, Delirium, Indulgence, Wealth"
favored-weapon: "Shortsword"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Dizzying Colors]], Rank 3: [[Enthrall]], Rank 5: [[Cloak Of Colors]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Blithe Spirit, Thisamet, exemplifies the warmth of celebration. In her merriment, she takes many forms and adjusts each to match the event. Often, she appears as a middle-aged woman with laugh lines worn deep in her face. She delights in attending events without fanfare, walking amongst mortal celebrants and immersing herself in the crowd. It's only as she leaves that the other celebrants notice the sheen of divinity remaining.

Other deities recognize the blessings she brings with her and she's always a favored guest. When she sits down to a feast, the table is never empty of food nor merrymakers. Instead, it seems to stretch to accommodates any and all who would partake. She flits from feast to feast, celebrating with all and welcoming any who would come to her table. In her presence, all grudges are set aside with a ban on intentional harm during the event. If there is a moment of accidental injury, she is quick to forgive. However, she is just as quick to eject those who purposefully violate the rules of the table. While only a few Firebrands worship Thisamet alone, many more invoke her to protect celebrations and ensure the safety of all in attendance.

**Title** The Blithe Spirit

**Areas of Concern** Celebrations, feasts, and holidays

**Edicts** Celebrate freely, share prosperity, invite all to your table

**Anathema** Ruin a holiday, quarrel at a feast, ignore workers when celebrating

**Religious Symbol** cornucopia of food

**Sacred Animal** cow

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
