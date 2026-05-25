---
type: deity
source-type: "Remaster"
domains: "Creation, Healing, Nature, Repose"
favored-weapon: "Hatchet"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Soothe]], Rank 3: [[Cozy Cabin]], Rank 5: [[Plant Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Immonhiel is an angel and patron goddess of medicine, herbs, and healing. Her teachings are widespread throughout the Realm of the Mammoth Lords, even among followings who don't revere the goddess herself. Immonhiel's worship is particularly prevalent among followings who eschew magic, as her balms are entirely natural, using only alterations of the natural world to work miracles.

Immonhiel is a wanderer with no fixed home, much like the people of the Realm. She travels the Material Plane and the celestial realms to heal all those in need. When recovery isn't possible, Immonhiel remains with the dying as long as she can, offering them comfort through their final hours and medicine to ease their pain and sorrow. The Balm-Bringer's followers aim to walk this same selfless path.

**Title** Balm-Bringer

**Areas of Concern** Herbs, medicine, plants, solace

**Edicts** Provide aid to the sick and wounded, grow or tend plants with healing properties, comfort the dying

**Anathema** Purposefully spread illness, destroy nature, abandon the wounded or dying

**Religious Symbol** leaf behind an open hand

**Sacred Animal** wolf

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
