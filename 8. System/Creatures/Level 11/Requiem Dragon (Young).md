---
type: creature
group: ["Divine", "Dragon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Requiem Dragon (Young)"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Divine"
trait_02: "Dragon"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+24; [[Darkvision]], [[Lifesense]] (imprecise) 60 feet, [[Scent]] (imprecise) 60 feet"
languages: "Chthonian, Common, Daemonic, Draconic, Empyrean, Requian"
skills:
  - name: Skills
    desc: "Acrobatics +19, Athletics +23, Diplomacy +21, Medicine +26, Religion +23, River of Souls Lore +21"
abilityMods: ["+7", "+4", "+5", "+4", "+7", "+5"]
abilities_top:
  - name: "Soul Journey"
    desc: "The dragon spends 1 hour traveling through planar channels to reach the River of Souls, and then reaches any point along the river. This has the effects of [[Interplanar Teleport]], except that the dragon can arrive precisely where they like on any major plane."
  - name: "Status Sight"
    desc: "The requiem dragon automatically knows the Hit Points of all creatures they can see."
  - name: "Draconic Momentum"
    desc: "The dragon recharges their Dooming Breath whenever they score a critical hit with a Strike."
armorclass:
  - name: AC
    desc: "30; **Fort** +21, **Ref** +18, **Will** +24"
health:
  - name: HP
    desc: "190; **Immunities** death effects, paralyzed, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Divine"
    desc: ""
  - name: "Soul Anchor"
    desc: "`pf2:r` A creature within 60 feet would drop to 0 Hit Points <br>  <br> **Effect** The dragon anchors the triggering creature's soul to its body. The creature remains at 1 Hit Point, becomes [[Doomed]] 2, and gains fast healing equal to the dragon's level for 1 minute. The creature becomes temporarily immune to further Soul Anchor usages for 24 hours. <br>  <br> > [!danger] Effect: Soul Anchor"
  - name: "Withhold Death"
    desc: "`pf2:r` **Trigger** The dragon is critically hit by an attack <br>  <br> **Effect** The dragon resists the loosening of its own soul, preventing some of the damage. The dragon gains resistance 10 to all damage against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Horn +24 (`pf2:1`) (magical, reach 10 ft.), **Damage** 2d10+10 piercing plus 1d8 spirit"
  - name: "Melee strike"
    desc: "Claw +24 (`pf2:1`) (agile, magical), **Damage** 2d8+10 slashing plus 1d8 spirit plus [[Grab]]"
  - name: "Melee strike"
    desc: "Tail +22 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d8+10 bludgeoning plus 1d8 spirit"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 27, attack +0<br>**1st** [[Heal]], [[Heal]], [[Stabilize]]"
abilities_bot:
  - name: "Dooming Breath"
    desc: "`pf2:2` Energy from Creation's Forge erupts from the dragon's mouth, dealing @Damage[9d8[spirit]|options:area-damage] damage in a @Template[type:line|distance:60] (DC 30 [[Reflex]] save). Undead creatures who fail the save must also succeed at a DC 30 [[Will]] save or become [[Doomed]] 1. If the target is already doomed, the doomed value increases by 1 (to a maximum of [[Doomed]] 4). The dragon can't use Dooming Breath again for 1d4 rounds."
  - name: "Draconic Frenzy"
    desc: "`pf2:2` The dragon makes two claw strikes and one tail strike in any order."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Requiem dragons are stewards of the River of Souls and the process through which souls reach their final destination in the afterlife. The safe journey of a soul is of utmost importance to a requiem dragon, and some will follow individual souls from their first entry into the river through to their judgment in the Boneyard and eventually to their ultimate resting place. Most requiem dragons tie themselves to specific planes and shepherd any souls bound to that plane, leading to dragons linked to places like Heaven or Hell, though these dragons never swear true allegiance to these planes. Requiem dragons fill their lairs along the River of Souls—patchworks of somber architecture rescued from other planes—with invaluable records and mementos of great accomplishments.

```statblock
creature: "Requiem Dragon (Young)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
