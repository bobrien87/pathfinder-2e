---
type: creature
group: ["Beast", "Primal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Grisantian Lion"
level: "12"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Beast"
trait_02: "Primal"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+25; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: "Common (Can't speak any language)"
skills:
  - name: Skills
    desc: "Acrobatics +22, Athletics +25, Intimidation +25, Stealth +22, Survival +22"
abilityMods: ["+7", "+5", "+7", "-3", "+4", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "32; **Fort** +25, **Ref** +22, **Will** +19"
health:
  - name: HP
    desc: "215; **Immunities** disease; **Resistances** fire 10, physical 10 except bludgeoning"
abilities_mid:
  - name: "Vicious Rend"
    desc: "`pf2:r` **Trigger** The grisantian lion uses Rend <br>  <br> **Effect** The target's armor takes damage equal to the damage from Rend. The target can attempt a DC 29 [[Reflex]] save to reduce this damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +26 (`pf2:1`) (unarmed), **Damage** 3d10+14 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +26 (`pf2:1`) (agile, unarmed), **Damage** 3d8+12 slashing"
spellcasting: []
abilities_bot:
  - name: "Blinding Mane"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** Drawing upon the power of their grogrisant ancestor, the grisantian lion focuses and causes their mane to glow with bright light. All creatures within 20 feet must attempt a DC 29 [[Fortitude]] save. <br> - **Critical Success** The target is unaffected. <br> - **Success** The target is [[Blinded]] until its next turn begins. <br> - **Failure** The target is blinded for 1 minute. <br> - **Critical Failure** The target is blinded permanently."
  - name: "Dual Pounce"
    desc: "`pf2:2` The grisantian lion Strides and makes two claw Strikes against the same creature at the end of that movement. Each attack counts against the grisantian lion's multiple attack penalty, but the penalty doesn't increase until after the grisantian lion makes both attacks. If both attacks hit, combine their damage for the purpose of resistances and weaknesses."
  - name: "Rend"
    desc: "`pf2:1` claw. <br>  <br> If the grisantian lion Rends after a successful Dual Pounce, combine the Rend's damage with that from the Dual Pounce for the purpose of resistances and weaknesses. <br>  <br> A Rend entry lists a Strike the monster has. <br>  <br> **Requirements** The monster hit the same enemy with two consecutive Strikes of the listed type in the same round. <br>  <br> **Effect** The monster automatically deals that Strike's damage again to the enemy."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The appearance of the mighty grogrisant is a once-in-a-generation event, but the descendants of those legendary beasts are well known along the World's Edge Mountains and throughout Taldor. These primal predators don't travel in a pride as mundane lions do. Instead, they avoid others of their kind, even to mate, and seek out ordinary lions once a year for this purpose. A grisantian lioness who bears cubs only tends her offspring long enough for them to become self-sufficient—which takes but a few months, thanks to their kind's incredibly rapid growth and development.

A full-grown grisantian lion is as large as an elephant and exceedingly aggressive, hunting anything it comes across. While ordinary lions rely on stealth and pack tactics to secure a meal, the grisantian lion is too big to hide amid tall grass. Instead, it has adapted to the mountains, where it chooses a large, hard-to-reach cave as its home, often killing any creature unfortunate enough to already inhabit the place. A grisantian lion can track for miles and is a canny hunter, hiding along rocky cliffs and outcroppings as it stalks prey.

Although they're wild creatures that can never be tamed, grisantian lions understand Taldane and occasionally agree to help those who defend nature. However, such alliances are temporary and unreliable at best.

```statblock
creature: "Grisantian Lion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
