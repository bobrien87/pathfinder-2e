---
type: creature
group: ["Amphibious", "Plant"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Doldrums Heap"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Amphibious"
trait_02: "Plant"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Wavesense]] (precise) 120 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +21, Stealth +18"
abilityMods: ["+6", "+4", "+5", "-4", "+2", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +21, **Ref** +18, **Will** +15"
health:
  - name: HP
    desc: "300; **Immunities** critical hits, precision, unconscious; **Weaknesses** slashing 10; **Resistances** cold 10"
abilities_mid:
  - name: "Mirage Spores"
    desc: "300 feet. <br>  <br> The sargassum heap constantly produces a field of hallucinogenic spores that causes those affected to see the monster as whatever they desire most. Each creature within the emanation must succeed a DC 27 [[Will]] save or become [[Fascinated]] with the sargassum heap and compelled to move toward it on the creature's turn. Creatures fascinated this way are also [[Off Guard]]. If the sargassum heap attacks, the fascinated condition ends only for the creature that is attacked. On a successful save, a creature is temporarily immune to mirage spores for 24 hours."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tendrils +21 (`pf2:1`) (reach 15 ft.), **Damage** 2d12+10 bludgeoning plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Constrict"
    desc: "`pf2:1` @Damage[(1d12+10)[bludgeoning]], DC 28 [[Fortitude]] save <br>  <br> The monster deals the listed amount of damage to any number of creatures [[Grabbed]] or [[Restrained]] by it. Each of those creatures can attempt a basic Fortitude save with the listed DC."
  - name: "Draw In"
    desc: "`pf2:2` The doldrums heap attempts to [[Reposition]] up to three creatures it has [[Grabbed]] or [[Restrained]]. These attempts neither apply nor count toward the heap's multiple attack penalty. <br>  <br> It can move them into its own space, dealing @Damage[(1d12+10)[bludgeoning]] damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Though most sargassum heaps divide once they grow too large, occasionally a heap will continue to grow indefinitely. These "doldrum heaps" can tangle and immobilize ships, tearing them apart or feasting on the hapless passengers.

A sargassum heap is a mass of semi-intelligent seaweed that floats through the ocean, luring in its victims with hallucinogenic spores. Those affected by the spores are drawn towards the heap, envisioning their heart's desire. This might be a lost loved one, a child in need of help, an enchanting mermaid, the promise of dry land, and so on. Once their prey is close enough, the sargassum heap lashes out with its seaweed tendrils and crushes it to death.

```statblock
creature: "Doldrums Heap"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
