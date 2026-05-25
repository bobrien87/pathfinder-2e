---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Freedom, Might"
favored-weapon: "Spiked-gauntlet"
divine-font: "Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Tailwind]], Rank 3: [[Roaring Applause]], Rank 4: [[Winning Streak]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Marishi is an azata empyreal lord and the goddess of athletics and sport, enthusiastic competition, and joyous celebration. She takes joy from competitions, games, and contests of all kinds, including artistic contests, like dance-offs and art showcases; mental contests, like trivia and complex board games; athletic contests, like races and weightlifting; and organized sports. Regardless of the contest, Marishi believes participants should strive for victory, compete honorably, and show pride in their accomplishments and efforts. She believes the winners of any competition should celebrate their victory and be lauded by others, for such is the prize for triumph. Marishi teaches that competition and the ensuing revelry should be fun and safe, for no joy can come from bringing harm to others.

Like most azatas, Marishi values love, compassion, freedom, and independence. Yet she knows these virtues can't be forced upon mortals—instead, mortals must be guided to seize them for themselves. Thus, she acts as an advisor and divine example for those who worship her. Through competition, mortals learn to strive for their own success, push themselves beyond what they thought possible, and create their own triumphs. From victory, they learn celebration, accomplishment, and pride.

**Title** The Festival Queen

**Areas of Concern** Celebration, contests, sport

**Edicts** Celebrate success, compete honorably, strive for victory, show pride in your accomplishments

**Anathema** Bully a competitor; deny a worthy victor their celebration or reward; cheat at a competition, contest, game, or sport

**Religious Symbol** Swirling rainbow ribbons

**Sacred Animal** dove

**Sacred Colors** all

**Source:** `= this.source` (`= this.source-type`)
