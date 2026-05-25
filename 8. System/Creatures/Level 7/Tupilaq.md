---
type: creature
group: ["Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tupilaq"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Construct"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +15"
abilityMods: ["+2", "+6", "+4", "-5", "+3", "-5"]
abilities_top:
  - name: "Carver's Curse"
    desc: "When a tupilaq is created, the curse imparted by its creator manifests in the form of a single 3rd-rank primal spell the tupilaq can cast three times per day. The particular spell is a reflection of the creator's wish for vengeance. By default, and for a found or summoned tupilaq, this spell is [[Fireball]]."
armorclass:
  - name: AC
    desc: "26 (22 when broken); **Fort** +17, **Ref** +15, **Will** +12"
health:
  - name: HP
    desc: "90; **Immunities** mental"
abilities_mid:
  - name: "Construct Armor (Hardness 8)"
    desc: "Like normal objects, a tupilaq has Hardness. This Hardness reduces any damage it takes by an amount equal to the Hardness. <br>  <br> Once a tupilaq is reduced to less than half its Hit Points, or immediately upon being damaged by a critical hit, its construct armor breaks, it loses its Hardness, and its Armor Class is reduced to 22."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +19 (`pf2:1`) (agile, finesse), **Damage** 2d8+5 slashing plus [[Grab]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 24, attack +16<br>**3rd** [[Fireball]]"
abilities_bot:
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A tupilaq is an artistically crafted construct carved from animal bones (typically whale or walrus) and imbued with the express purpose of eviscerating its creator's enemies. A tupilaq manifests from hateful magic—such a thing can only be created by someone who believes they were grievously wronged. When a terrible, unforgivable crime is committed against someone with great skill at carving and who has knowledge of the proper ritual, the aggrieved can channel their grief and hate through whispered incantations to bring a tupilaq to life.

Sadly, the same emotions used to create a tupilaq often lead to even greater tragedies. Functionally immortal but built for vengeance, a tupilaq lacks the reason or discernment to do anything other than pursue the goal imbued by its creator. A wish to utterly destroy an enemy can lead a tupilaq to slaughter an entire settlement, killing until it has slain everyone even remotely related to the original offender. Many stories describe how a tupilaq ends up causing more tragedy for its creator than the crime that precipitated its creation. The most common tales feature the tupilaq eventually murdering its creator's spouse or family members due to a distant relationship to the original target that no one knew about.

A tupilaq's animating energies aren't tied to its original functions, and the creature typically long outlasts its creator, its victims, and often any who recall the reason for its creation. It might fall into a sort of hibernation once it has achieved immediate vengeance, but in many cases, the constructs reawaken to continue their rampage against unsuspecting targets ignorant of their involvement.

Spellcasters might occasionally summon these constructs. A summoned tupilaq, hauled unceremoniously from its vengeance, becomes a near-frenzied combatant, unleashing every offensive ability in its arsenal to break free. These reactions aren't strategic or considered, but an instinctual, almost programmed need to return to its true purpose. Conjurers should be wary about a tupilaq employing spells that might be turned against its summoner, such as a fireball "accidentally" placed such that the spell incinerates the spellcaster and returns the creatures from whence it came.

```statblock
creature: "Tupilaq"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
