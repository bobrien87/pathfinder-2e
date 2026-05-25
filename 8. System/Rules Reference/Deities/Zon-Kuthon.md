---
type: deity
source-type: "Remaster"
domains: "Ambition, Darkness, Destruction, Pain"
favored-weapon: "Spiked-chain"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 3: [[Wall Of Thorns]], Rank 5: [[Umbral Journey]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

A being of pure malevolence that embodies and exalts pain, shadow, and mutilation, Zon-Kuthon is one of the most terrifying entities to inspire worship on Golarion. The Midnight Lord teaches that darkness and envy, loss and pain are sacraments. Through inflicting and enduring torment, the worshipper seizes true strength. Experiencing pain in all of its forms allows the devout to cut away the weakness of the body, mind, and spirit. Instead of fearing or avoiding pain, the Kuthite embraces it, yields to it, wields it. Beyond pain comes release, power, and mastery.

**Title** The Midnight Lord

**Areas of Concern** darkness, envy, loss, pain

**Edicts** bring pain to the world, mutilate your body

**Anathema** create permanent or long-lasting sources of light, provide comfort to those who suffer

**Religious Symbol** chained skull

**Sacred Animal** bat

**Sacred Colors** dark gray, red

**Source:** `= this.source` (`= this.source-type`)
