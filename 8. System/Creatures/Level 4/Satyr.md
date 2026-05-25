---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Satyr"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Low-Light Vision]]"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Athletics +8, Deception +13, Diplomacy +13, Intimidation +11, Nature +9, Performance +13, Stealth +11, Survival +8"
abilityMods: ["+3", "+4", "+1", "+1", "+2", "+5"]
abilities_top:
  - name: "Sylvan Wine"
    desc: "A satyr's wineskin magically enchants any alcohol inside. With an Interact action, a living creature can imbibe the alcohol and gain a +1 item bonus to Will saves and a +3 item bonus to Will saves against fear effects for the following hour. When the wineskin is removed from a satyr's person, the magic remains only until the wine spoils. The wineskin holds up to eight drafts of wine. <br>  <br> > [!danger] Effect: Sylvan Wine"
  - name: "Fleet Performer"
    desc: "When the satyr Plays the Pipes to cast a spell, he can Step or Stride as part of the activity."
armorclass:
  - name: AC
    desc: "19; **Fort** +9, **Ref** +11, **Will** +12"
health:
  - name: HP
    desc: "80; **Weaknesses** cold iron 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+6 piercing"
  - name: "Melee strike"
    desc: "Dagger +14 (`pf2:1`) (agile, thrown 10, versatile s), **Damage** 1d4+6 piercing"
  - name: "Ranged strike"
    desc: "Shortbow +14 (`pf2:1`) (deadly d10, reload 0, range 60 ft.), **Damage** 1d6+3 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 21, attack +13<br>**4th** [[Suggestion]]<br>**2nd** [[Triple Time]]<br>**1st** [[Charm]], [[Courageous Anthem]], [[Fear]], [[Figment]], [[Light]], [[Sleep]], [[Uplifting Overture]]"
abilities_bot:
  - name: "Play the Pipes"
    desc: "`pf2:3` **Requirements** The satyr is holding a musical instrument. <br>  <br> **Effect** The satyr plays a melody on his instrument to cast [[Charm]], [[Fear]], [[Sleep]], or [[Suggestion]] without expending the spell slot. <br>  <br> The spell gains the auditory trait and targets all creatures in a @Template[emanation|distance:60] instead of its usual targets. A creature that succeeds at its Will save against any spell is then temporarily immune from spells played from that satyr's pipes for 1 minute. Satyrs are immune to this music."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

To a satyr, life is a party and everyone is invited. Notorious for their hedonism, these fey believe there's no greater beauty than can be found in song, drink, indulgent meals, and carnal pleasures. Satyrs use their enchanting songs and natural charm to encourage all manner of people to follow their true desires and free themselves from society's rules. This usually involves enticing mortals to join raucous parties or engage in trysts in moonlit glades. If a potential companion rejects a satyr's advances, however, the satyr has little interest in continuing a conversation and goes off to find more amenable revelers.

The lifestyle of a satyr leaves no room for ongoing affairs or long-term friends. Once his party is over or his lust is satiated, the satyr disappears back into the forest. The offspring satyrs leave behind are satyrs themselves, and they usually end up being taken from their cradles by other fey rather than left in mortals' care. Satyrs are always male.

The untouched beauty of the forest is sacred and precious to a satyr. Brutish intruders who clear-cut trees or massacre animals without eating them risk drawing a satyr's ire. A satyr so provoked uses his spells to undermine foes and attempts to dispatch them either with brutal ambushes or by leading a rush of forest animals to attack.

Other fey, particularly more benevolent fey, look upon satyrs as loutish, embarrassing cousins. They're rarely hostile toward satyrs, but most find them insufferable and advise any mortals they like to steer clear of satyrs' glades.

```statblock
creature: "Satyr"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
