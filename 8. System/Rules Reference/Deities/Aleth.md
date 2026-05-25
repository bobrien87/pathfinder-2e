---
type: deity
source-type: "Remaster"
domains: "Darkness, Family, Protection, Secrecy"
favored-weapon: "Shield-boss"
divine-font: "Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 3: [[Wall Of Shadow]], Rank 7: [[Shadow Raid]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Aleth is the god of the solace, wonder, and mystery found in darkness, and of the way that communities and families come together at night. When a gentle shade provides relief against heat stroke and the glaring sun, Aleth dwells in that darkness. So too does she provide a gentle shroud of privacy in the cover of darkness, hiding the embarrassed blush of two young lovers' cheeks, allowing them to express their feelings away from the public eye. In this way, Aleth represents the infinite possibilities and mysteries that exist in the darkness, while protecting all within her embrace from the harsh light of the public eye.

**Title** The Gentle Shroud

**Areas of Concern** community, hospitality, mystery, night

**Edicts** offer hospitality to travelers who arrive at your abode at night, protect others from the harshness of the light, seek out the infinite mysteries hidden in the darkness

**Anathema** expose others' privacy, speak a truth that is more harmful than silence, violate hospitality once offered

**Religious Symbol** cloak of darkness limned in purple

**Sacred Animal** brown bat

**Sacred Colors** black, purple

**Source:** `= this.source` (`= this.source-type`)
