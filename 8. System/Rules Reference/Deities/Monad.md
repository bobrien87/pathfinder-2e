---
type: deity
source-type: "Remaster"
domains: "Creation, Knowledge, Void, Truth"
favored-weapon: "Fist"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Phantasmal Minion]], Rank 2: [[Ghostly Carrier]], Rank 4: [[Vapor Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

All aeons come from, return to, are connected with, and are guided by the Monad. The Condition of All is not a deity in the traditional sense. It exists both within and outside the multiverse and has influence over the entirety of existence. Though generally content to allow the multiverse to run its course, the Monad directs its aeons to intervene when events deviate from their ineffable design. Mortal scholars often personify the Monad as the deity of creation, the infinite, and truth. Even so, few worship it, and the Monad pays very little attention to mortal petitioners. Instead, scholars study and plot aeons' actions, striving to discern the Monad's ultimate goal or to uncover universal truths they can exploit for their own purposes. Only a rare few mortals can master the asceticism necessary to connect with the Monad, gaining hidden knowledge and powers akin to those of other divine spellcasters. While the Monad seems to be more than capable of maintaining the sanctity of existence, the fact that it broke off pieces of itself to create the first arbitrators suggests the Monad is either fully incapable of doing so alone or is choosing to focus its attention toward other matters.

**Title** The Condition of All

**Areas of Concern** Creation, the infinite, truth

**Edicts** Ensure balance between opposing forces, mediate disagreements

**Anathema** Allow your personal motivations to determine a major decision

**Religious Symbol** spiral galaxy

**Sacred Animal** trilobite

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
