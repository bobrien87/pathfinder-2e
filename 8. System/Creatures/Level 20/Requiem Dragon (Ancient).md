---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Requiem Dragon (Ancient)"
level: "20"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+36; [[Darkvision]], [[Lifesense]] (imprecise) 120 feet, [[Scent]] (imprecise) 60 feet"
languages: "Chthonian, Common, Daemonic, Draconic, Empyrean, Requian"
skills:
  - name: Skills
    desc: "Acrobatics +32, Athletics +38, Diplomacy +34, Medicine +41, Religion +38, River of Souls Lore +34"
abilityMods: ["+10", "+6", "+7", "+6", "+10", "+7"]
abilities_top:
  - name: "Soul Journey"
    desc: "The dragon spends 1 hour traveling through planar channels to reach the River of Souls, and then reaches any point along the river. This has the effects of [[Interplanar Teleport]], except that the dragon can arrive precisely where they like on any major plane."
  - name: "Status Sight"
    desc: "The requiem dragon automatically knows the Hit Points of all creatures they can see."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Dooming Breath whenever they score a critical hit with a Strike."
armorclass:
  - name: AC
    desc: "44; **Fort** +33, **Ref** +30, **Will** +36"
health:
  - name: HP
    desc: "370; **Immunities** death effects, paralyzed, sleep"
abilities_mid:
  - name: "Soul Anchor"
    desc: "`pf2:r` A creature within 60 feet would drop to 0 Hit Points <br>  <br> **Effect** The dragon anchors the triggering creature's soul to its body. The creature remains at 1 Hit Point, becomes [[Doomed]] 2, and gains fast healing equal to the dragon's level for 1 minute. The creature becomes temporarily immune to further Soul Anchor usages for 24 hours. <br>  <br> > [!danger] Effect: Soul Anchor"
  - name: "Withhold Death"
    desc: "`pf2:r` **Trigger** The dragon is critically hit by an attack <br>  <br> **Effect** The dragon resists the loosening of its own soul, preventing some of the damage. The dragon gains resistance 20 to all damage against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +38 (`pf2:1`) (magical, reach 20 ft.), **Damage** 4d10+15 piercing plus 2d8 spirit"
  - name: "Melee strike"
    desc: "Claw +38 (`pf2:1`) (agile, magical, reach 15 ft.), **Damage** 4d6+15 slashing plus 2d8 spirit plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +36 (`pf2:1`) (magical, reach 25 ft.), **Damage** 4d8+15 bludgeoning plus 2d8 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 39, attack +0<br>**1st** [[Heal]], [[Heal]], [[Stabilize]]"
abilities_bot:
  - name: "Dooming Breath"
    desc: "`pf2:2` Energy from Creation's Forge erupts from the dragon's mouth, dealing @Damage[16d8[spirit]|options:area-damage] damage in a @Template[type:line|distance:120] (DC 42 [[Reflex]] save). Undead creatures who fail the save must also succeed at a DC 42 [[Will]] save or become [[Doomed]] 1. If the target is already doomed, the doomed value increases by 1 (to a maximum of [[Doomed]] 4). The dragon can't use Dooming Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw strikes and one tail strike in any order."
  - name: "Redirect River"
    desc: "`pf2:1` The requiem dragon redirects a small portion of the River of Souls, using their body as a spiritual connection. The river swells around them, filling the area in a @Template[type:emanation|distance:15] for 1 round, becoming difficult terrain to all other creatures. Additionally, creatures that begin their turn in the emanation or enter it for the first time each round must succeed a DC 42 [[Fortitude]] save or become [[Drained]] 1 and [[Doomed]] 1. If the target is already drained or doomed, the value increases by 1 (to a maximum of 4). The dragon can Sustain the effect."
  - name: "Soul Shield"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The requiem dragon uses their life essence to create a shield of spiritual energy around a creature within 60 feet. The shield creates a link between the dragon and the creature with the effects of [[Share Life]] except that the effect doesn't end regardless of distance and remains for 1 hour. In addition, the creature gains resistance 10 to physical and spirit damage that applies to the half of damage it receives. The dragon can Dismiss the effect."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Requiem dragons are stewards of the River of Souls and the process through which souls reach their final destination in the afterlife. The safe journey of a soul is of utmost importance to a requiem dragon, and some will follow individual souls from their first entry into the river through to their judgment in the Boneyard and eventually to their ultimate resting place. Most requiem dragons tie themselves to specific planes and shepherd any souls bound to that plane, leading to dragons linked to places like Heaven or Hell, though these dragons never swear true allegiance to these planes. Requiem dragons fill their lairs along the River of Souls—patchworks of somber architecture rescued from other planes—with invaluable records and mementos of great accomplishments.

```statblock
creature: "Requiem Dragon (Ancient)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
