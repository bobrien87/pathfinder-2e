---
type: deity
source-type: "Remaster"
domains: "Healing, Nature, Change, Water"
favored-weapon: "Machete"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Plant Or Fungus]], Rank 3: [[Cozy Cabin]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Aminara champions the rushes, reeds, and fallen trees that flourish along waterways' banks. She delights in floodplains and placid, meandering streams, yet her passion lies in oxbow lakes and wetlands that form as plants and deposited silt transform the landscape.

Aminara encourages her faithful to act with similar patience and flexibility. A dedicated follower must understand that there will be delays, snags, and diversions—all reminders to savor the quiet moments and not rush. Like a gentle river, a worshipper's gentle kindness and wisdom can build communities filled with friends more numerous than cattails.

After being displaced by Taldor's long-ago expansion and their wetland reclamation project, Aminara wandered the greater Sellen River basin for millennia. In recent centuries, she's returned to her old home—Taldor's neglected canal network. Amid its silt-choked waterways, she has nurtured long gardens of new growth that delight visitors. Yet, officials know that if they try to restore too many canals to working order, they might risk an ancient demigod's wrath.

**Title** Lady of Reeds

**Areas of Concern** Aquatic plants, detours, wetlands

**Edicts** Relish life's quiet moments, foster the growth and well-being of flora, reshape surroundings to create new ecosystems and opportunities

**Anathema** Needlessly rush or take a direct route when you could wander, destroy healthy wetlands, harm plant life except in the pursuit of saving greater plant life

**Religious Symbol** trio of cattails forming a triangle

**Sacred Animal** dragonfly

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
