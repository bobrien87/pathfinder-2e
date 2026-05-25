---
type: deity
source-type: "Remaster"
domains: "Cities, Family, Knowledge, Perfection"
favored-weapon: "Shield-boss"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Share Lore]], Rank 4: [[Shape Stone]], Rank 5: [[Wall Of Stone]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Mazludeh was once one among many empyreal lords, responsible for the domains of community stewardship and loving sacrifice. However, her actions during Earthfall and the Age of Darkness saved untold lives in Mwangi. Dismayed by the chaos and loss of life, Mazludeh spurred her fellow empyreal lords into action, forming a divine concordance that protected the Garundi nation of Holomog from devastation. Mazludeh's efforts elevated her to true divinity and the status of the matron goddess of the nation of Holomog. Now the goddess of negotiations and treaties, her followers often travel with merchants and ambassadors. She is also considered the diplomat to the other empyreal lords, able to pass on prayers to those most suited to answer them and persuade celestial beings to see to their fulfillment. Throughout the Mwangi, worshippers of Mazludeh have developed a reputation for being brave, empathetic, and fair even to their enemies.

**Title** Mother of Hearth and Wall

**Areas of Concern** Balance, community, negotiation, and twilight

**Edicts** Seek to improve yourself and your community, trust those you work with, encourage cooperation

**Anathema** Betray another's trust, place conflict between ideological differences over people's lives

**Religious Symbol** Seven eggs encircled by an ouroboros

**Sacred Animal** anaconda

**Sacred Colors** pink, green

**Source:** `= this.source` (`= this.source-type`)
