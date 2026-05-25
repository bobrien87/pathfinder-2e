---
type: deity
source-type: "Remaster"
domains: "Destruction, Freedom, Indulgence, Zeal"
favored-weapon: "Spiked-gauntlet"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Summon Animal]], Rank 4: [[Reflective Scales]], Rank 7: [[Unfettered Pack]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Petitioners to Anogetz understand that there is no such thing as a bloodless revolution. Even if the turning point of a war for one's community was diplomatic, the road to reach such a transition was built upon the corpses of all the freedom fighters who died before they could see the tomorrow they wished for. By granting their followers the opportunity to act as raging beasts against hated foes, the Fated Fangs gluts themself on the ensuing havoc.

**Title** The Fated Fangs

**Areas of Concern** Animal attacks, coups, revolution

**Edicts** Be as merciless (or more so) as your oppressors, indulge as beasts indulge, let your rage fuel your deeds

**Anathema** Refrain from harming an oppressor's loved ones, spare a tyrant's life

**Religious Symbol** animal fangs on a crown

**Sacred Animal** all

**Sacred Colors** gold, red

**Source:** `= this.source` (`= this.source-type`)
