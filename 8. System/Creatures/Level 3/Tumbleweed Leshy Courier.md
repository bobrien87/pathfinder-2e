---
type: creature
group: ["Leshy", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tumbleweed Leshy Courier"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Leshy"
trait_02: "Plant"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+12; [[Low-Light Vision]]"
languages: "Common, Fey (speak with plants (tumbleweeds and scrubland brush only))"
skills:
  - name: Skills
    desc: "Acrobatics +11, Diplomacy +8, Nature +10, Society +7, Stealth +9, Survival +10"
abilityMods: ["+1", "+4", "+1", "+0", "+2", "+2"]
abilities_top:
  - name: "Tumbling Traveler"
    desc: "The tumbleweed leshy courier gains a +10-foot circumstance bonus to Speed while traveling during exploration mode."
armorclass:
  - name: AC
    desc: "19; **Fort** +6, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "35"
abilities_mid:
  - name: "Nimble Dodge"
    desc: "`pf2:r` **Trigger** The tumbleweed leshy courier is targeted with an attack by an attacker they can see <br>  <br> **Effect** The leshy gains a +2 circumstance bonus to AC against the triggering attack."
  - name: "Spiny Burst"
    desc: "When the tumbleweed leshy courier dies, a burst of primal energy explodes from their body, restoring @Damage[2d8[healing,vitality]|shortLabel] Hit Points to each plant creature in a @Template[type:emanation|distance:30]. This area immediately fills with brambles and thistles, becoming difficult terrain. Any creature that moves through the area takes 1 piercing damage per square traversed. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +11 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+5 piercing"
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +12 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+2 piercing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 17, attack +0<br>**3rd** [[Speak with Plants (tumbleweeds and scrubland brush only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The tumbleweed leshy courier transforms into a Small tumbleweed. This ability otherwise uses the effects of [[One with Plants]]. Additionally, when the leshy uses their Change Shape ability, they still have a Speed of 10 feet for the purpose of travel during exploration mode. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

A tumbleweed leshy's ability to move quickly across long distances with ease allows them to act as messengers and go-betweens. Druids often entrust these couriers with delivering important messages to their home druid circles or other druids they're acquainted with. Some even induct the couriers into the circle to teach them Wildsong for secure communication and basic magic for self-defense.

Nature spirits inhabit bodies made of plants or fungi, blooming from primal magic to become the small people called leshies. They come in a truly immense number of diverse shapes and sizes, more so than most peoples of Golarion. This variety of forms means a leshy could have a place in nearly any type of setting for any type of story.

```statblock
creature: "Tumbleweed Leshy Courier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
