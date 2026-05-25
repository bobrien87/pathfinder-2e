---
type: creature
group: ["Leshy", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Gourd Leshy Witch"
level: "6"
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
languages: "Common, Fey (speak with plants (gourds only))"
skills:
  - name: Skills
    desc: "Acrobatics +12, Intimidation +13, Nature +14, Occultism +16, Survival +12"
abilityMods: ["+2", "+2", "+1", "+4", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "22; **Fort** +11, **Ref** +14, **Will** +14"
health:
  - name: HP
    desc: "80"
abilities_mid:
  - name: "Verdant Burst"
    desc: "When the gourd leshy witch dies, a burst of primal energy explodes from their body, restoring @Damage[4d8[healing,vitality]|shortLabel] Hit Points to each plant creature in a @Template[type:emanation|distance:30]. This area immediately fills with gourds, becoming difficult terrain. If the terrain is not a viable environment for these plants, they wither after 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Broom +13 (`pf2:1`) (magical, two hand d8), **Damage** 1d4+6 bludgeoning plus 1d6 void"
  - name: "Melee strike"
    desc: "Dagger +12 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+6 piercing plus 1d6 void"
  - name: "Melee strike"
    desc: "Dagger +12 (`pf2:1`) (agile, finesse, thrown 10, versatile s), **Damage** 1d4+6 piercing plus 1d6 void"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning plus 1d6 void"
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 24, attack +16<br>**3rd** (3 slots) [[Force Barrage]], [[Slow]], [[Vampiric Feast]]<br>**2nd** (3 slots) [[Force Barrage]], [[Grim Tendrils]], [[Paranoia]]<br>**1st** (3 slots) [[Fear]], [[Fear]], [[Ill Omen]]<br>**Cantrips** [[Daze]], [[Detect Magic]], [[Figment]], [[Shield]], [[Void Warp]]"
  - name: "Primal Innate Spells"
    desc: "DC 24, attack +0<br>**3rd** [[Speak with Plants (Gourds Only)]] (Constant)"
  - name: "Witch Hex Spells"
    desc: "DC 24, attack +0<br>**1st** [[Wilding Word]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The gourd leshy witch transforms into a Small gourd. This ability otherwise uses the effects of [[One with Plants]]. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Short Flight"
    desc: "`pf2:1` `pf2:1` to `pf2:2` <br>  <br> **Frequency** once per round <br>  <br> **Requirements** The gourd leshy witch is wielding a broom <br>  <br> **Effect** The gourd leshy hops on their broom, which briefly takes flight. The witch Flies 20 feet (or 40 feet if they spend 2 actions), though they must end this movement on solid ground or fall at the end of their turn."
  - name: "Sweeping Spell"
    desc: "`pf2:1` **Requirements** The gourd leshy witch is wielding their broom <br>  <br> **Effect** If the next action the gourd leshy witch uses is to cast a non-cantrip spell that deals damage to a single target, the witch's broom flies out and attempts to `act shove options=sweeping-spell` that creature with an Athletics modifier of +16. On a critical success, the target is also knocked [[Prone]]. The broom immediately returns to the gourd leshy witch's hand."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Some spooky leshies learn the ways of occult spellcasting from strange spirits of nature that lurk just out of sight or under cover of darkness. These witches treat their brooms as their familiars, imbuing the wood and straw with a sliver of sentience.

Nature spirits inhabit bodies made of plants or fungi, blooming from primal magic to become the small people called leshies. They come in a truly immense number of diverse shapes and sizes, more so than most peoples of Golarion. This variety of forms means a leshy could have a place in nearly any type of setting for any type of story.

```statblock
creature: "Gourd Leshy Witch"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
