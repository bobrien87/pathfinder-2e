---
type: deity
source-type: "Remaster"
domains: "Confidence, Glyph, Magic, Truth"
favored-weapon: "Claw, Khakkhara"
divine-font: "Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Phantasmal Minion]], Rank 2: [[Telekinetic Maneuver]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

More than her kin, Yluma wielded magic with power. Magical currents coursed through her body, filling her frame with the power to raise mountains and level entire plains. Yet each awe-inspiring act came at an incredible cost. With each miraculous feat, Yluma's form changed, becoming less distinct and whole. Yluma shared her fears with her father, but the Waybringer could do nothing to stop this change. He confided that in Yluma he could see a fragment of Sarshallatu's infinity. Yluma's body, no matter how powerful, would eventually be torn at the seams, unable to contain her mother's unbound vastness. And so, Yluma vowed to seek out Sarshallatu, hoping that her mother would help her get rid of such a curse. She traveled far and wide across the edges of creation. Her frame, pulled and stretched by the trials she faced, seemed on the verge of collapse when she finally reached her mother's lonely refuge. She gazed upon her divine mother, trying to take in all her vastness and power. Yluma looked at herself, feeling the soreness of her powerful muscles, tired and aching after the long journey. She traced the scars left by her battles, remembering how she bested all those who opposed her using her gifts. And she understood.

So, she returned to her kin, her body a monument to her triumphs and failures. She etched her knowledge and insights on her scales, giving her body a new shape, a magical frame that kept herself whole. Yluma's careful talons now shape the form of each arcane dragon, taking care to enshrine their essence within the patterns of their scales to make sure that they do not struggle as she struggled.

**Title** The Living Page

**Areas of Concern** knowledge, magic, self-acceptance

**Edicts** celebrate your victories and losses, embrace your unique strengths and innate gifts, nurture the flame of acceptance and knowledge in others.

**Anathema** intentionally mislead people away from understanding themselves, repeatedly deny who you are, treat your gifts as a curse

**Religious Symbol** a talon-tipped quill writing on a pale dragon scale

**Sacred Animal** non-venomous snake

**Sacred Colors** black and pale yellow

**Source:** `= this.source` (`= this.source-type`)
