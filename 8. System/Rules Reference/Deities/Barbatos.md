---
type: deity
source-type: "Remaster"
domains: "Magic, Nature, Travel, Tyranny"
favored-weapon: "Staff"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Spider Sting]], Rank 3: [[Paralyze]], Rank 4: [[Clairvoyance]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Barbatos is the youngest of the archdevils, and in fact is not truly a devil at all. His true nature remains unknown and perpetually cloaked, but when he appeared at Hell's gates bearing the souls of an entire mortal world and transformed them into Hell's first legion of barbazus as an offering, the Prince of Darkness saw fit to grant Barbatos rulership over Hell's first layer, Avernus. As Hell's doorwarden, Barbatos oversees the spaces between worlds, and his followers are those who tread such interstitial paths and hold no qualms about the ethics of their journeys.

**Title** The Bearded Lord

**Areas of Concern** Animals, corruption, gateways

**Edicts** Veil your motives, make dangerous deals, offer incomplete and ruinous knowledge

**Anathema** Hide any plot against your masters, close or interfere with portals to Hell

**Religious Symbol** three-eyed beard

**Sacred Animal** raven

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
