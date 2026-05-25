---
type: deity
source-type: "Remaster"
domains: "Ambition, Duty, Knowledge, Secrecy"
favored-weapon: "Sword-cane"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Mindlink]], Rank 3: [[Time Pocket]], Rank 5: [[Synaptic Pulse]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Based in Ustalav but active in aristocratic salons and cloistered academies across Avistan and Garund, the Esoteric Order of the Palatine Eye is a mystic order of occultist-nobles who seek philosophical self-awareness and mastery of celestial truths. The order was founded in 3988 AR when the gentleman-explorer Aldus Canter returned from the Osirian desert where he had been lost for 3 years. Aldus spoke of meeting a cult following a desiccated angel named Tabris. Tabris revealed the secret history of the multiverse and tasked Aldus with acting as a messenger of mystic secrets. Upon his return, Aldus gathered a coterie of his fellow Ustalavic nobles eager to plumb these secrets. His message was far from clear, however, consisting of garbled and coded texts in an untidy medley of Osirian mysticism, Pharasmin rites, and Varisian occult lore. Scouring Aldus's texts-both those brought from Osirion and his many annotations and reinterpretations penned thereafter-has been the order's primary activity for centuries, even before the increasingly erratic Aldus disappeared in 4028 AR. The Esoteric Order's meticulous research has produced occult secrets and mystical rites known nowhere else on Golarion and hints at further secret lore for the enlightened. The order's greatest accomplishment, however, was averting a doomsday few on Golarion will ever realize was imminent: in 4718 AR, the order's greatest heroes prevented the planet Aucturn from devouring Golarion.

**Covenant Members** mysterious forces

**Areas of Concern** history, occultism, secret lore

**Edicts** honor the rites of the Order while pushing for change, provide succor to scholars and truth-seekers, pursue the wisdom of ancient forgotten texts such as The Lost Gospels of Tabris

**Anathema** destroy rare or ancient lore, dismiss or remain ignorant to the newly found texts, reveal the Order's secrets to those outside the organization

**Religious Symbol** golden scarab beetle with outstretched wings revealing an eye

**Source:** `= this.source` (`= this.source-type`)
