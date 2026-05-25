---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Duty, Fate"
favored-weapon: "Mace"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Enthrall]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Pantheon Members** Apsu, Narriseminek, Shizuru

**Areas of Concern** rulership, judgment, lineage, fated authority

**Edicts** pursue perfection in yourself and others, help others seize their destiny, search for lost rulers

**Anathema** refuse a promotion, work against the fulfillment of prophecy, kill the last member of a noble line

**Religious Symbol** plume of orange and blue fire above a crown

A movement worshipping these strange divine bedfellows as guardians of destiny and rulership has emerged since the Godsrain. With political, social, and military matters unsettled, acolytes of the Anointing of Kings yearn for a time of strong leaders and certain predictions. Some search hidden record books and genealogical libraries in hopes of finding worthy heirs that have been overlooked by the ages, while others seek personal power, hoping to ascend to thrones and rule over dominions. While all followers of the pantheon value ascension to glory and monarchy, significant disagreement simmers about how to achieve this goal. Those who favor Apsu and Shizuru advocate for slowing gathering power and legitimacy in hopes of a diplomatic takeover. Narriseminek's faithful scoff at such incrementalist methods and push for the violent overthrow of regimes they don't consider legitimate.

**Source:** `= this.source` (`= this.source-type`)
