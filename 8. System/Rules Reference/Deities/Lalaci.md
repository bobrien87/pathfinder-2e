---
type: deity
source-type: "Remaster"
domains: "Change, Introspection, Luck, Sun"
favored-weapon: "Sling"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Dizzying Colors]], Rank 3: [[Hypnotize]], Rank 4: [[Peaceful Bubble]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

He of Motley Repose champions not only the beauties that are rainbows and relaxation, but also the true importance of self-worth. He teaches that the only way to truly find rest is to know and value oneself above all else. His worshippers are known best for being protectors of the oasis in the desert, for Lalaci knows that having a safe place to rest and relax is just as important as taking the time to be self-reflective and understand yourself. Those who are not protectors use the beauty and versatility of the sands to create works of art, which attempt to mimic the perfect reflection of color found in the beauty of rainbows that come after a storm.

**Title** He of Motley Repose

**Areas of Concern** Rainbows, relaxation, self-worth, shade

**Edicts** Wear a rainbow every day, hang suncatchers in different places for everyone to see, take and provide opportunities to rest and relax

**Anathema** Pretend to be someone that you're not, prevent someone from taking time for themselves, refuse to listen to both sides of an argument

**Religious Symbol** rainbow with shadow

**Sacred Animal** lacewing

**Sacred Colors** all

**Source:** `= this.source` (`= this.source-type`)
