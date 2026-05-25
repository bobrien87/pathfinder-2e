---
type: creature
group: ["Agathion", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Procyal"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Agathion"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean, Halfling (speak with animals, truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Deception +18, Diplomacy +16, Medicine +16, Nature +16, Religion +16, Society +17, Stealth +16, Survival +16, Thievery +14, Nirvana Lore +15"
abilityMods: ["+4", "+4", "+6", "+5", "+6", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Raccoon's Whimsy"
    desc: "Procyals' core value is whimsy, though unlike for chaotic tricksters, procyals' playful actions have a pattern and their pranks always come with a valuable lesson, even if it takes a long time to decipher the meaning. Receiving and growing from such a lesson requires at least 10 minutes of interaction with the Procyal but can take much longer. A character who learns from the procyal's lesson gains the benefits of the [[Aid]] reaction from the procyal once during the next month. Afterwards, they become immune to this effect from all procyals."
armorclass:
  - name: AC
    desc: "26; **Fort** +16, **Ref** +14, **Will** +18"
health:
  - name: HP
    desc: "170; **Weaknesses** unholy 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Claw +18 (`pf2:1`) (agile, holy, magical, unarmed), **Damage** 2d8+10 slashing plus 1d6 spirit"
  - name: "Melee strike"
    desc: "Shortsword +19 (`pf2:1`) (agile, finesse, holy, magical, versatile s), **Damage** 2d6+10 piercing plus 1d6 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 26, attack +18<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Suggestion]] (At Will), [[Translocate]]<br>**3rd** [[Heroism]]<br>**2nd** [[Calm]], [[Dispel Magic]], [[Illusory Creature]], [[Invisibility]], [[Speak with Animals]] (Constant)<br>**1st** [[Charm]]"
  - name: "Champion Focus Spells"
    desc: "DC 26, attack +18<br>**1st** [[Lay on Hands]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The procyal can transform only into a specifc individual Small or Medium humanoid that they've met at least once. They can't transform into a generic member of a given ancestry. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

As the most whimsical and playful of the agathions, procyals are the most likely to be encountered in the Universe, teaching deep philosophical lessons and delivering wisdom through pranks and impersonations. Mischievous and playful, these raccoon-headed humanoids love to socialize with mortals and learn about their societies. Unlike their mortal counterparts, procyals' fur starts off dark russet in color, giving way to gray and white fecks on their muzzles as they grow older. Only procyal leaders boast the stark gray and black coloration of a true raccoon. Those who recognize procyals' age and wisdom treat these creatures with great respect.

Whatever their natural appearance, procyals make excellent shapeshifters and can assume the form of any humanoid that they've encountered. They use this ability for only the greater good of that humanoid or their community, often appearing as someone's trusted mentor to deliver an important message in a more laid-back fashion than talking to a magical celestial raccoon. They're not above playing the occasional harmless prank on the person whose form they've assumed, especially when they can use it to teach a valuable lesson. Raccoon agathions prefer to use a blade if forced into combat, but they're prepared to use their claws and fght dirty if necessary.

```statblock
creature: "Procyal"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
