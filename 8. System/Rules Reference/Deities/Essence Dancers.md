---
type: deity
source-type: "Remaster"
domains: "Creation, Wyrmkin, Knowledge, Magic"
favored-weapon: "Claw, Tekko-kagi"
divine-font: "Harm, Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Mindlink]], Rank 3: [[Hypercognition]], Rank 5: [[Summon Dragon]], Rank 8: [[Quandary]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Pantheon Members** Brixori, Garhaazh, Turvu, Yluma

**Areas of Concern** the cosmos, ley lines, magic, synthesis

**Edicts** pursue fundamental truths, compare your experience to that of others, investigate new solutions

**Anathema** become stagnant or passive in your thinking, abandon magic, sequester useful discoveries or valuable information

**Religious Symbol** four intertwined dragons

Magical theory describes the four fundamental magical essences—life, matter, mind, and spirit—that undergird the practice of magic as it's known today, with the essences bound together in a dance of complex interactions to form the four traditions of magic. Followers of the Essence Dancers not only seek to understand these interactions but also see the dragon gods as embodiments of these forces and guides toward transcendent understanding of magic and the cosmos. Worship of the pantheon recently began at the Magaambya, likely a syncretistic combination of beliefs from visiting Taralu dwarven scholars and from scholars on the blending of arcane and primal magic traditions. Carried by travelers investigating magical phenomena or tracing the course of ley lines, the pantheon quickly spread across Golarion. Such pilgrimages are common among the faithful; journeys are undertaken in pairs, with ideal traveling partners wielding magic covering the spectrum of magical essences, such as a druid and bard traveling together. Congregations of the faithful are led by a tetrad, four worshippers who together command all four traditions of magic.

**Source:** `= this.source` (`= this.source-type`)
