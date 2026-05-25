---
type: creature
group: ["Aberration", "Amphibious"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dibrasgorth"
level: "13"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]]"
languages: "Chthonian, Common, Diabolic, Draconic, Empyrean"
skills:
  - name: Skills
    desc: "Acrobatics +18, Arcana +20, Athletics +25, Nature +17, Occultism +20, Religion +17, Stealth +20, Survival +19"
abilityMods: ["+8", "+1", "+4", "+5", "+2", "+0"]
abilities_top:
  - name: "Planar Sight"
    desc: "The eyes at the end of their tentacles allow a dibrasgorth to see into planes coterminous with the one it is currently on at the listed range. For instance, if they're in the Universe, they can see into the Ethereal Plane and the Netherworld."
  - name: "Draining Bite"
    desc: "A dibrasgorth feeds on the spirits of its victims. A creature that is damaged by the dibrasgorth's jaws Strike must attempt a DC 30 [[Fortitude]] save or become [[Drained]] 1 ([[Drained]] 2 on a critical failure). In addition, the dibrasgorth gains 10 temporary Hit Points that last for 1 minute if the creature fails or critically fails the save. <br>  <br> > [!danger] Effect: Draining Bite"
  - name: "Transdimensional Tentacles"
    desc: "The dibrasgorth can worm its tentacles through nearby planes to attack. While in the Universe, its tentacle Strikes ignore all cover from objects unless those objects exist on both the Universe and either the Netherworld or the Ethereal Plane, or the objects have the extradimensional trait."
armorclass:
  - name: AC
    desc: "33 all-around vision; **Fort** +26, **Ref** +20, **Will** +23"
health:
  - name: HP
    desc: "250; **Immunities** death effects, polymorph, petrified; **Resistances** acid 15, cold 15, mental 15"
abilities_mid:
  - name: "All-Around Vision"
    desc: "This monster can see in all directions simultaneously and therefore can't be flanked."
  - name: "Warped Space"
    desc: "100 feet. The dibrasgorth's presence distorts the fabric of space. Any other creature who uses a teleportation effect or spell within the aura must attempt a DC 33 [[Fortitude]] save or become [[Sickened]] 2."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`) (magical, reach 20 ft.), **Damage** 3d10+16 piercing plus [[Draining Bite]]"
  - name: "Melee strike"
    desc: "Tentacle +27 (`pf2:1`) (agile, magical, reach 20 ft.), **Damage** 3d8+16 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 33, attack +0<br>**7th** [[Interplanar Teleport]]<br>**6th** [[Dominate]], [[Repulsion]]<br>**5th** [[Banishment]], [[Synaptic Pulse]]<br>**4th** [[Nightmare]], [[Suggestion]]<br>**2nd** [[See the Unseen]] (Constant)<br>**1st** [[Daze]]"
abilities_bot:
  - name: "Breath of Phantasms"
    desc: "`pf2:2` The dibrasgorth exhales a @Template[type:cone|distance:60] of noxious gas. Each creature in the area takes @Damage[7d6[poison]|options:area-damage] damage (DC 30 [[Fortitude]] save). On a failure, the creature is also [[Confused]] for 1 round (or 2 rounds on a critical failure)."
  - name: "Drag Through Dimensions"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The dibrasgorth has a creature [[Grabbed]] or [[Restrained]] with a tentacle <br>  <br> **Effect** The dibrasgorth's tentacle whips through coterminous planes as it smashes the creature it is holding against the ground and other natural features in each plane before returning to this plane. The creature takes 5d8 bludgeoning damage (DC 30 [[Reflex]] save). A creature who fails the save is also [[Stupefied 1]] for 1 round and [[Sickened]] 1 by the rapid planar travel."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Dibrasgorths, sometimes called Mothers of Oblivion, are monstrous creatures of chaos who dwell in lightless spaces, often near the bottom of deep lakes and oceans both above and underground. They may look like hideous monsters with heads like a plesiosaur atop masses of tentacles, each tipped with a baleful red eye, but dibrasgorths have a twisted sense of cunning, likely due to their ability to see into and affect planes other than the one where they stand. Though they are quite powerful (with some the favored servants of Lamashtu), dibrasgorths prefer to keep their existence a secret from the mortals of the world above.

```statblock
creature: "Dibrasgorth"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
